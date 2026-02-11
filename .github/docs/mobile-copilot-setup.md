# Mobile Copilot Field Capture Setup

This guide explains how to set up GitHub Personal Access Token (PAT) for mobile field captures using GitHub Copilot.

## Problem

When GitHub Copilot creates PRs from mobile, it uses GitHub App credentials that don't trigger CI workflows due to GitHub's security measures (prevents infinite workflow loops). This leaves PRs stuck in a "pending checks" state.

## Solution

We've implemented a two-part solution:

### 1. Auto-Trigger Workflow (Already Set Up)

The workflow `.github/workflows/bot-pr-ci-trigger.yml` automatically:
- Detects when a bot (Copilot/GitHub Actions) creates a PR
- Pushes an empty commit using a PAT
- Triggers all CI checks
- Adds a comment to the PR

### 2. Create Personal Access Token (PAT)

To enable the auto-trigger workflow to bypass GitHub's security restriction, you need to create a PAT:

#### On Your Phone (Mobile Browser)

1. **Navigate to GitHub Settings:**
   - Go to https://github.com/settings/tokens
   - Or: Profile → Settings → Developer settings → Personal access tokens → Fine-grained tokens

2. **Create New Token:**
   - Click "Generate new token" → "Fine-grained token"
   - Token name: `BOT_CI_TRIGGER_PAT`
   - Expiration: 90 days (or custom)
   - Repository access: "Only select repositories" → choose `career-intelligence-space`

3. **Set Permissions:**
   - Repository permissions:
     - **Contents**: Read and write (to push commits)
     - **Pull requests**: Read (to check PR info)
     - **Workflows**: Read and write (to trigger workflows)

4. **Generate and Copy:**
   - Click "Generate token"
   - **IMPORTANT**: Copy the token immediately (starts with `github_pat_`)
   - You won't be able to see it again!

5. **Add to Repository Secrets:**
   - Go to: https://github.com/jwade83/career-intelligence-space/settings/secrets/actions
   - Click "New repository secret"
   - Name: `BOT_CI_TRIGGER_PAT`
   - Value: Paste your token
   - Click "Add secret"

## Usage

Once set up, just use your normal workflow:

1. Fill out field capture in ChatGPT mobile
2. Get the Copilot instructions from ChatGPT
3. Paste into GitHub Copilot in mobile browser
4. Copilot creates the PR
5. The auto-trigger workflow automatically:
   - Pushes an empty commit
   - Triggers all CI checks
   - Adds a comment explaining what happened
6. CI passes → PR auto-merges (if automerge enabled)

## Troubleshooting

### PR Still Stuck in Pending
- Check if the PAT secret is correctly named `BOT_CI_TRIGGER_PAT`
- Verify PAT has correct permissions
- Check workflow runs: https://github.com/jwade83/career-intelligence-space/actions

### Workflow Not Running
- Ensure the workflow file exists: `.github/workflows/bot-pr-ci-trigger.yml`
- Check if PR was created by a bot (check PR author)
- Look for errors in Actions tab

### PAT Expired
- You'll get an email from GitHub
- Create a new PAT following steps above
- Update the repository secret

## Security Notes

- **Never share your PAT** - treat it like a password
- Use fine-grained tokens (not classic tokens) for better security
- Set reasonable expiration dates (90 days recommended)
- Only grant minimum required permissions
- Scope to specific repository only

## Future Improvements

Possible enhancements:
- Auto-renew PAT before expiration
- Notification when PAT is about to expire
- Alternative: GitHub App with installation token

