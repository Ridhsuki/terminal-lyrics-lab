# Terminal Lyrics Lab

Terminal Lyrics Lab is a small collection of terminal-based lyric experiments.

This repository contains simple code for displaying lyrics in the terminal using timed text.

## Structure

Each lyric project is placed in its own folder inside `tracks/`.

```txt
terminal-lyrics-lab/
├── README.md
└── tracks/
    ├── 001-song-title/
    │   ├── main.py
    │   ├── README.md
    │   └── lyrics.lrc
    │
    └── 002-another-song/
        ├── main.js
        ├── README.md
        └── lyrics.lrc
````

Folder names use this format:

```txt
001-song-title
002-another-song
003-next-song
```

## How to Run

Clone this repository:

```bash
git clone https://github.com/Ridhsuki/terminal-lyrics-lab.git
cd terminal-lyrics-lab
```

Open a track folder:

```bash
cd tracks/001-shitsunaikei-trackmaker
```

Run the file based on the language used in that folder.

Example for Python:

```bash
python3 main.py
```

Example for JavaScript:

```bash
node main.js
```

Check the `README.md` inside each track folder for specific instructions.

## Request a Lyric

Anyone can request a new lyric by opening an [issue](https://github.com/Ridhsuki/terminal-lyrics-lab/issues).

Please include:

* Song title
* Artist name
* Any notes or preferred effect

## Contributing

Contributions are welcome.

You can fork this repository and open a pull request to add a new lyric project.

Basic steps:

```bash
git fork
git checkout -b add-new-lyric
```

Add your lyric project inside `tracks/`, then commit your changes:

```bash
git add .
git commit -m "feat: add new lyric experiment"
git push origin add-new-lyric
```

Then open a pull request.
