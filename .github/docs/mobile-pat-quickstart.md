# Mobile PAT Setup - Quick Start

**5-Minute Setup** (Do this once, works forever)

## 📱 On Your Phone

### 1. Create Token (2 min)
```
🔗 https://github.com/settings/tokens?type=beta
```

Tap: **"Generate new token"**

**Settings:**
- Name: `BOT_CI_TRIGGER_PAT`
- Expiration: `90 days`
- Repository: `Only select repositories` → `career-intelligence-space`

**Permissions:**
- ✅ Contents: `Read and write`
- ✅ Pull requests: `Read`
- ✅ Workflows: `Read and write`

Tap: **"Generate token"**

### 2. Copy Token (30 sec)
**COPY THE TOKEN NOW!** (Starts with `github_pat_...`)

💡 Tip: Paste into Notes app temporarily if needed

### 3. Add to Repository (1 min)
```
🔗 https://github.com/jwade83/career-intelligence-space/settings/secrets/actions/new
```

- Name: `BOT_CI_TRIGGER_PAT`
- Secret: [Paste your token]
- Tap: **"Add secret"**

## ✅ Done!

Your mobile field captures will now auto-trigger CI checks!

---

## 🎯 Normal Usage (After Setup)

1. **ChatGPT**: Fill field capture template
2. **ChatGPT**: Get Copilot instructions  
3. **GitHub Mobile Browser**: Paste into Copilot
4. **Copilot**: Creates PR
5. **Auto-magic**: Workflow triggers CI
6. **Auto-magic**: PR merges when checks pass

---

## 📋 Links Cheat Sheet

| Action | Link |
|--------|------|
| Create PAT | https://github.com/settings/tokens?type=beta |
| Add Secret | https://github.com/jwade83/career-intelligence-space/settings/secrets/actions/new |
| View Secrets | https://github.com/jwade83/career-intelligence-space/settings/secrets/actions |
| Check Workflows | https://github.com/jwade83/career-intelligence-space/actions |

---

## 🔐 Security

- ✅ Fine-grained token (limited scope)
- ✅ Single repository only
- ✅ 90-day expiration
- ✅ Minimum permissions
- ⚠️ Never commit PAT to repository
- ⚠️ Never share in screenshots/messages

---

## 🆘 Troubleshooting

**PR stuck in pending?**
→ Check: https://github.com/jwade83/career-intelligence-space/settings/secrets/actions
→ Verify secret named exactly: `BOT_CI_TRIGGER_PAT`

**Workflow not running?**
→ Check: https://github.com/jwade83/career-intelligence-space/actions
→ Look for "Bot PR CI Trigger" workflow

**Token expired?**
→ Repeat steps 1-3 above
→ Update existing secret (don't create new)

