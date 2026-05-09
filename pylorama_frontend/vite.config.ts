import { defineConfig } from 'vite';

export default defineConfig({
   build: {
      outDir: '../products/static/scripts',
      rollupOptions: {
         input: 'src/table.ts',
         output: {
            entryFileNames: 'table.js',
         },
      },
   },
});