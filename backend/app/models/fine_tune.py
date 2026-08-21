# 1. Set Git Identity
git config --global user.name "Vishakha"
git config --global user.email "vishakha@example.com"

# 2. Initialize Git (if not already)
git init

# 3. Add all files
git add .
# Or add specific files
git add README.md
git add backend/
git add frontend/
git add database/
# Add all other files and folders

# 4. Check what's staged
git status

# 5. Commit the changes
git commit -m "Initial commit: AIOPS-FORGE Enterprise AI Platform"

# 6. Rename branch to main (if needed)
git branch -M main

# 7. Add remote repository
git remote add origin https://github.com/vishakha2121/AIOPS-FORGE.git

# 8. Push to GitHub
git push -u origin main

# 9. If you have tags, push them too
git push --tags