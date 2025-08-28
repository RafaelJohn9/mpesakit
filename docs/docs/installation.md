---
title: "Installation"
sidebar_label: "Installation"
---

# Installation

`gh-templates` is a Rust-based CLI tool that can be installed through various methods.

## Installation Methods

### Homebrew (macOS/Linux)

```bash
brew install RafaelJohn9/tap/gh-templates
```

### PyPI

```bash
pip install gh-templates
```

### npm

```bash
npm install -g gh-templates
```

### Cargo

```bash
cargo install gh-templates
```

This will download, compile, and install the latest version of `gh-templates` to your Cargo bin directory (usually `~/.cargo/bin`).

### Quick Install (directly from github releases)

Install `gh-templates` automatically with a single command:

**Linux/macOS:**

```bash
curl -sSL https://raw.githubusercontent.com/RafaelJohn9/gh-templates/main/install/install.sh | bash
```

**Windows (PowerShell):**

```powershell
iwr -useb https://raw.githubusercontent.com/RafaelJohn9/gh-templates/main/install/install.ps1 | iex
```

✅ The installer automatically:

- Detects your OS and architecture
- Downloads the latest version
- Installs to the appropriate location (`~/.local/bin` on Linux/macOS, `~/bin` on Windows)
- Makes the binary executable

> **Note:** Ensure your install directory is in your `PATH`. On Linux/macOS, you may need to add `export PATH="$HOME/.local/bin:$PATH"` to your shell profile.

---

## Manual Installation

If you prefer to install manually, download the appropriate binary for your platform from the [GitHub Releases](https://github.com/RafaelJohn9/gh-templates/releases) page:

<details>
<summary>Linux (x86_64, glibc) - Most common</summary>

```bash
wget https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>Linux (x86_64, musl) - Alpine Linux, static builds</summary>

```bash
wget https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>Linux (x86, 32-bit glibc) - Older systems</summary>

```bash
wget https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>Linux (x86, 32-bit musl) - Alpine Linux 32-bit</summary>

```bash
wget https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>Linux (ARM64, glibc) - Raspberry Pi 4, ARM servers</summary>

```bash
wget https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>Linux (ARM64, musl) - Alpine Linux on ARM64</summary>

```bash
wget https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>macOS (Apple Silicon) - M1, M2, M3+ Macs</summary>

```bash
curl -LO https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>macOS (Intel) - Pre-2020 Macs</summary>

```bash
curl -LO https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates
chmod +x gh-templates
mkdir -p ~/.local/bin
mv gh-templates ~/.local/bin/
```

</details>

<details>
<summary>Windows (x86_64) - 64-bit Windows</summary>

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"
Invoke-WebRequest -Uri "https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates.exe" -OutFile "$env:USERPROFILE\bin\gh-templates.exe"
```

> **Note:** Make sure `$env:USERPROFILE\bin` is in your `PATH` environment variable.

**Alternative using curl (if available):**

```cmd
mkdir "%USERPROFILE%\bin"
curl -LO https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates.exe
move gh-templates.exe "%USERPROFILE%\bin\"
```

</details>

<details>
<summary>Windows (x86, 32-bit) - Older Windows systems</summary>

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"
Invoke-WebRequest -Uri "https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates.exe" -OutFile "$env:USERPROFILE\bin\gh-templates.exe"
```

> **Note:** Make sure `$env:USERPROFILE\bin` is in your `PATH` environment variable.

</details>

<details>
<summary>Windows (ARM64) - Surface Pro X, Windows on ARM</summary>

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"
Invoke-WebRequest -Uri "https://github.com/RafaelJohn9/gh-templates/releases/latest/download/gh-templates.exe" -OutFile "$env:USERPROFILE\bin\gh-templates.exe"
```

> **Note:** Make sure `$env:USERPROFILE\bin` is in your `PATH` environment variable.

</details>

### Adding to PATH

After installation, you may need to add the binary location to your PATH:

<details>
<summary>Linux/macOS - Adding ~/.local/bin to PATH</summary>

Add this line to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload your shell:

```bash
source ~/.bashrc  # or ~/.zshrc
```

</details>

<details>
<summary>Windows - Adding to PATH</summary>

1. **Via System Properties (GUI):**
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Click "Environment Variables"
   - Under "User variables", select "Path" and click "Edit"
   - Click "New" and add `%USERPROFILE%\bin`
   - Click OK to save

2. **Via PowerShell (Command):**

   ```powershell
   $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
   [Environment]::SetEnvironmentVariable("Path", "$userPath;$env:USERPROFILE\bin", "User")
   ```

3. **Restart your terminal** for changes to take effect.

</details>

---

## Verify Installation

After installation, verify that `gh-templates` is working correctly:

```bash
gh-templates --version
```

You should see output similar to:

```
gh-templates 0.1.0
```

After installation, verify that `gh-templates` is working correctly:

```bash
gh-templates --version
```

You should see output similar to:

```
gh-templates 0.1.0
```

## Build Information

To see detailed build information about your installation:

```bash
gh-templates --build-info
```

This displays compilation details and other build metadata.

The `--force` flag ensures the existing installation is overwritten with the new version.

## Next Steps

Now that you have `gh-templates` installed, check out the [Usage Guide](./usage.md) to learn how to use it effectively.
