import { copyFile, mkdir, mkdtemp, rename, rm } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const files = ['index.html', 'remaker-test.html', 'remaker-mockup.html',
  'avulio-assets/laboratorio.css', 'avulio-assets/mark.svg', 'avulio-assets/una-domanda.webp'];
const temp = await mkdtemp(join(root, '.avulio-build-'));
try {
  for (const file of files) {
    const target = join(temp, file);
    await mkdir(dirname(target), { recursive: true });
    await copyFile(join(root, file), target);
  }
  const output = join(root, 'dist');
  await rm(output, { recursive: true, force: true });
  await rename(temp, output);
} finally {
  await rm(temp, { recursive: true, force: true });
}
