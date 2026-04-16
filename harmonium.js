/**
 * Web Harmonium Simulator - Logic
 * (c) 2026 Hao Ling Sheng
 */

class HarmoniumEngine {
    constructor() {
        this.audioCtx = null;
        this.masterGain = null;
        this.activeNotes = new Map(); // midiNote -> { oscillators, gainNodes }
        this.isStarted = false;
        
        // Settings
        this.rootPitch = 60; // C4
        this.reedType = 'double';
        this.bellowsPressure = 0;
        this.targetPressure = 0;
        
        // Drone
        this.droneActive = false;
        this.droneOscs = [];
        this.droneGain = null;
        // Recording
        this.recorder = null;
        this.recordedChunks = [];
        this.isRecording = false;
        this.dest = null;
    }

    init() {
        if (this.isStarted) return;
        this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        this.masterGain = this.audioCtx.createGain();
        this.masterGain.gain.value = 0.5;
        
        // Final destination for recording
        this.dest = this.audioCtx.createMediaStreamDestination();
        this.masterGain.connect(this.dest);
        this.masterGain.connect(this.audioCtx.destination);
        
        this.isStarted = true;
        this.initMIDI();
        
        // Bellows Loop
        this.updateBellows();
    }

    initMIDI() {
        if (navigator.requestMIDIAccess) {
            navigator.requestMIDIAccess().then(
                (midi) => this.setupMIDI(midi),
                () => console.log("MIDI Access Denied")
            );
        }
    }

    setupMIDI(midi) {
        for (let input of midi.inputs.values()) {
            input.onmidimessage = (msg) => this.handleMIDIMessage(msg);
        }
    }

    handleMIDIMessage(msg) {
        const [status, note, velocity] = msg.data;
        const cmd = status >> 4;
        const channel = status & 0xf;

        if (cmd === 9 && velocity > 0) { // Note On
            this.playNote(note);
        } else if (cmd === 8 || (cmd === 9 && velocity === 0)) { // Note Off
            this.stopNote(note);
        }
    }

    updateBellows() {
        // Natural air pressure simulation
        const decay = 0.95;
        const growth = 0.2;
        
        if (this.activeNotes.size > 0 || this.droneActive) {
            this.targetPressure = 0.8;
        } else {
            this.targetPressure = 0;
        }
        
        this.bellowsPressure = this.bellowsPressure * decay + this.targetPressure * (1 - decay);
        
        // Update UI indicator
        const fill = document.getElementById('bellows-fill');
        if (fill) fill.style.width = (this.bellowsPressure * 100) + '%';
        
        requestAnimationFrame(() => this.updateBellows());
    }

    getFrequency(midiNote) {
        return 440 * Math.pow(2, (midiNote - 69) / 12);
    }

    playNote(midiNote) {
        if (!this.isStarted) this.init();
        if (this.activeNotes.has(midiNote)) return;

        const freq = this.getFrequency(midiNote);
        const gainNode = this.audioCtx.createGain();
        gainNode.gain.setValueAtTime(0, this.audioCtx.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.3, this.audioCtx.currentTime + 0.05);
        gainNode.connect(this.masterGain);

        const oscs = [];
        
        // Layer 1: Bass Reed (Square)
        const osc1 = this.audioCtx.createOscillator();
        osc1.type = 'square';
        osc1.frequency.setValueAtTime(freq / 2, this.audioCtx.currentTime);
        osc1.connect(gainNode);
        osc1.start();
        oscs.push(osc1);

        // Layer 2: Male Reed (Sawtooth)
        if (this.reedType !== 'single') {
            const osc2 = this.audioCtx.createOscillator();
            osc2.type = 'sawtooth';
            osc2.frequency.setValueAtTime(freq, this.audioCtx.currentTime);
            const g2 = this.audioCtx.createGain();
            g2.gain.value = 0.4;
            osc2.connect(g2);
            g2.connect(gainNode);
            osc2.start();
            oscs.push(osc2);
        }

        // Layer 3: Female Reed (Thin Square)
        if (this.reedType === 'triple') {
            const osc3 = this.audioCtx.createOscillator();
            osc3.type = 'square';
            osc3.frequency.setValueAtTime(freq * 2, this.audioCtx.currentTime);
            const g3 = this.audioCtx.createGain();
            g3.gain.value = 0.2;
            osc3.connect(g3);
            g3.connect(gainNode);
            osc3.start();
            oscs.push(osc3);
        }

        this.activeNotes.set(midiNote, { oscs, gainNode });
        
        // Highlight UI
        const keyEl = document.querySelector(`.key[data-note="${midiNote}"]`);
        if (keyEl) keyEl.classList.add('active');
    }

    stopNote(midiNote) {
        if (!this.activeNotes.has(midiNote)) return;

        const { oscs, gainNode } = this.activeNotes.get(midiNote);
        gainNode.gain.linearRampToValueAtTime(0, this.audioCtx.currentTime + 0.15);
        
        setTimeout(() => {
            oscs.forEach(o => o.stop());
            gainNode.disconnect();
        }, 200);

        this.activeNotes.delete(midiNote);
        
        const keyEl = document.querySelector(`.key[data-note="${midiNote}"]`);
        if (keyEl) keyEl.classList.remove('active');
    }

    toggleTanpura(type) {
        if (!this.isStarted) this.init();
        
        if (this.droneActive) {
            if (this.droneGain) {
                this.droneGain.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + 1);
                const oldGain = this.droneGain;
                const oldOscs = this.droneOscs;
                setTimeout(() => {
                    oldOscs.forEach(o => o.stop());
                    oldGain.disconnect();
                }, 1100);
            }
            this.droneOscs = [];
            this.droneActive = false;
            return false;
        }

        this.droneGain = this.audioCtx.createGain();
        this.droneGain.gain.setValueAtTime(0, this.audioCtx.currentTime);
        this.droneGain.gain.linearRampToValueAtTime(0.2, this.audioCtx.currentTime + 1);
        this.droneGain.connect(this.masterGain);

        const fundamental = this.getFrequency(this.rootPitch - 24); // Low drone
        const notes = [fundamental, fundamental * 1.5, fundamental * 2]; // Sa Pa Sa
        
        if (type === 'MA') notes[1] = fundamental * (4/3);
        if (type === 'NI') notes[1] = fundamental * (15/8);

        notes.forEach(f => {
            const osc = this.audioCtx.createOscillator();
            osc.type = 'triangle';
            osc.frequency.value = f;
            osc.detune.value = Math.random() * 10 - 5;
            osc.connect(this.droneGain);
            osc.start();
            this.droneOscs.push(osc);
        });

        this.droneActive = true;
        return true;
    }

    toggleRecord() {
        if (!this.isStarted) this.init();

        if (this.isRecording) {
            this.recorder.stop();
            this.isRecording = false;
            return false;
        }

        this.recordedChunks = [];
        this.recorder = new MediaRecorder(this.dest.stream);
        
        this.recorder.ondataavailable = (e) => {
            if (e.data.size > 0) this.recordedChunks.push(e.data);
        };

        this.recorder.onstop = () => {
            const blob = new Blob(this.recordedChunks, { type: 'audio/webm' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'harmonium-recording.webm';
            document.body.appendChild(a);
            a.click();
            setTimeout(() => {
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            }, 100);
        };

        this.recorder.start();
        this.isRecording = true;
        return true;
    }
}

// UI Handling
const engine = new HarmoniumEngine();
const keyboard = document.getElementById('keyboard');
const sargamNotes = ['Sa', 're', 'Re', 'ga', 'Ga', 'Ma', 'ma', 'Pa', 'dha', 'Dha', 'ni', 'Ni'];
const westernNotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

function generateKeyboard() {
    keyboard.innerHTML = '';
    const startNote = 48; // C3
    const endNote = 84;   // C6
    
    for (let n = startNote; n <= endNote; n++) {
        const isBlack = [1, 3, 6, 8, 10].includes(n % 12);
        const key = document.createElement('div');
        key.className = `key ${isBlack ? 'black' : 'white'}`;
        key.dataset.note = n;
        
        // Labels
        const label = document.createElement('div');
        label.className = 'key-label';
        label.innerText = westernNotes[n % 12];
        key.appendChild(label);

        const sargam = document.createElement('div');
        sargam.className = 'sargam-label';
        // Logic for rotating sargam based on root
        // For simplicity, we'll implement this update function
        key.appendChild(sargam);

        // Interaction
        key.onmousedown = (e) => { e.preventDefault(); engine.playNote(n); };
        key.onmouseup = () => engine.stopNote(n);
        key.onmouseleave = () => engine.stopNote(n);
        key.ontouchstart = (e) => { e.preventDefault(); engine.playNote(n); };
        key.ontouchend = () => engine.stopNote(n);

        keyboard.appendChild(key);
    }
    updateSargamLabels();
}

function updateSargamLabels() {
    const rootSelect = document.getElementById('scale-root');
    if (!rootSelect) return;
    
    const root = parseInt(rootSelect.value);
    document.querySelectorAll('.key').forEach(key => {
        const note = parseInt(key.dataset.note);
        const diff = (note - root + 120) % 12;
        const sLabel = key.querySelector('.sargam-label');
        if (sLabel) sLabel.innerText = sargamNotes[diff];
    });
    updateRagaHighlight();
}

const ragas = {
    bilaval: [0, 2, 4, 5, 7, 9, 11],
    yaman: [0, 2, 4, 6, 7, 9, 11],
    bhairav: [0, 1, 4, 5, 7, 8, 11],
    kafi: [0, 2, 3, 5, 7, 9, 10],
    khamaj: [0, 2, 4, 5, 7, 9, 10],
    asavari: [0, 2, 3, 5, 7, 8, 10],
    bhairavi: [0, 1, 3, 5, 7, 8, 10],
    todi: [0, 1, 3, 6, 7, 8, 11]
};

function updateRagaHighlight() {
    const ragaSelect = document.getElementById('raga-select');
    const rootSelect = document.getElementById('scale-root');
    if (!ragaSelect || !rootSelect) return;

    const ragaKey = ragaSelect.value;
    const root = parseInt(rootSelect.value);
    const intervals = ragas[ragaKey] || null;

    document.querySelectorAll('.key').forEach(key => {
        key.classList.remove('highlight');
        if (intervals) {
            const note = parseInt(key.dataset.note);
            const diff = (note - root + 120) % 12;
            if (intervals.includes(diff)) {
                key.classList.add('highlight');
            }
        }
    });
}

// Keyboard Mapping
const keyMap = {
    'a': 60, 'w': 61, 's': 62, 'e': 63, 'd': 64, 'f': 65, 't': 66, 'g': 67, 'y': 68, 'h': 69, 'u': 70, 'j': 71, 'k': 72,
    'q': 60, '2': 61, 'z': 48, 'x': 50, 'c': 52
};

window.onkeydown = (e) => {
    if (e.repeat) return;
    const note = keyMap[e.key.toLowerCase()];
    if (note) engine.playNote(note);
};

window.onkeyup = (e) => {
    const note = keyMap[e.key.toLowerCase()];
    if (note) engine.stopNote(note);
};

// Controls
document.getElementById('scale-root').onchange = (e) => {
    engine.rootPitch = parseInt(e.target.value);
    updateSargamLabels();
};

document.getElementById('raga-select').onchange = () => {
    updateRagaHighlight();
};

document.getElementById('reed-type').onchange = (e) => {
    engine.reedType = e.target.value;
};

const tanpuraBtn = document.getElementById('tanpura-btn');
tanpuraBtn.onclick = () => {
    const active = engine.toggleTanpura(document.getElementById('tanpura-note').value);
    tanpuraBtn.innerText = active ? 'STOP' : 'START';
    tanpuraBtn.classList.toggle('active', active);
};

const recordBtn = document.getElementById('record-btn');
recordBtn.onclick = () => {
    const active = engine.toggleRecord();
    recordBtn.innerText = active ? 'STOP' : 'REC';
    recordBtn.classList.toggle('active', active);
    document.getElementById('status').innerText = active ? 'RECORDING...' : 'SAVED';
};

// Metronome (simple version)
let metronomeInterval = null;
const metronomeBtn = document.getElementById('metronome-btn');
metronomeBtn.onclick = () => {
    if (metronomeInterval) {
        clearInterval(metronomeInterval);
        metronomeInterval = null;
        metronomeBtn.innerText = 'OFF';
        metronomeBtn.classList.remove('active');
    } else {
        if (!engine.isStarted) engine.init();
        metronomeInterval = setInterval(() => {
            const osc = engine.audioCtx.createOscillator();
            const g = engine.audioCtx.createGain();
            osc.frequency.value = 1000;
            g.gain.value = 0.1;
            osc.connect(g);
            g.connect(engine.masterGain);
            osc.start();
            osc.stop(engine.audioCtx.currentTime + 0.05);
        }, 500); // 120 BPM
        metronomeBtn.innerText = 'ON';
        metronomeBtn.classList.add('active');
    }
};

// Initialize
window.addEventListener('DOMContentLoaded', () => {
    generateKeyboard();
    console.log("Harmonium keyboard generated and UI ready.");
});
