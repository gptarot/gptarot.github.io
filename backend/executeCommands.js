const { exec } = require('child_process');

module.exports = (req, res) => {
  const shellScriptPath = './commands.sh';

  exec(`chmod +x ${shellScriptPath} && ${shellScriptPath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing the shell script: ${error.message}`);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }

    console.log('Shell script executed successfully.');
    // Handle the response as needed
    res.status(200).json({ message: 'Shell script executed successfully.', stdout, stderr });
  });
};
