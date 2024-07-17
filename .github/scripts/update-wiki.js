const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;

function getCommitMessages() {
  const commitMessages = execSync('git log -1 --pretty=%B').toString().trim();
  return commitMessages;
}

function parseCommitMessage(commitMessage) {
  const match = commitMessage.match(/\{Keyword\}: \[(.*)\] \{(.*)\} \{(.*)\} \{(.*)\}/);
  if (match) {
    return {
      keyword: match[1],
      issue: match[2],
      source: match[3],
      difficulty: match[4],
      title: match[5],
    };
  }
  return null;
}

function difficultyLevel(difficulty) {
  return parseInt(difficulty.replace('lv', ''), 10);
}

function updateWikiFile(commitDetails) {
  const wikiPath = path.resolve('../wiki/your-wiki-file.md');
  const date = new Date().toISOString().split('T')[0];
  const newEntry = `| ${commitDetails.difficulty} | [${commitDetails.title}](${commitDetails.source}) | ${date} |\n`;

  let fileContent = fs.readFileSync(wikiPath, 'utf-8');
  const lines = fileContent.split('\n');
  const headerIndex = lines.findIndex(line => line.startsWith('|---'));

  const sortedLines = [...lines.slice(headerIndex + 1), newEntry]
    .sort((a, b) => difficultyLevel(b.split('|')[1].trim()) - difficultyLevel(a.split('|')[1].trim()));

  const updatedContent = [...lines.slice(0, headerIndex + 1), ...sortedLines].join('\n');
  fs.writeFileSync(wikiPath, updatedContent);
}

function main() {
  const commitMessage = getCommitMessages();
  const commitDetails = parseCommitMessage(commitMessage);

  if (commitDetails && commitDetails.keyword.toLowerCase() === 'solve') {
    updateWikiFile(commitDetails);

    execSync('git config --global user.name "github-actions[bot]"');
    execSync('git config --global user.email "github-actions[bot]@users.noreply.github.com"');
    execSync('git add ../wiki/your-wiki-file.md');
    execSync(`git commit -m "Update wiki with new solve entry: ${commitDetails.title}"`);
    execSync('git push');
  }
}

main();
