const util = require('util');
const exec = util.promisify(require('child_process').exec);

async function getContainerId() {
  const { stdout, stderr } = await exec('docker ps | grep discovery');
  const out = stdout.trim().split('\n');
  let id = null;

  if (out.length > 0) {
    id = out[0].trim().split(' ')[0];
  }

  console.log(id);
}

if (require.main === module) {
  getContainerId();
}
