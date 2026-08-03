# Install and Commit

From Downloads:

```bash
cd ~/Downloads
unzip STK-00_0-v1.0.zip
cd STK-00_0-v1.0
chmod +x install_and_commit.sh
./install_and_commit.sh
```

Default target: `~/KOP-Labs/00_0-master-document-governance`

The script requires:
- `~/KOP-Labs` is an existing Git repository
- clean Git working tree
- configured `origin`
- no existing target directory
- no existing local tag `STK-00_0-v1.0`
