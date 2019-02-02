module.exports = function(grunt) {

  grunt.initConfig({
    'validation': { // Grunt w3c validation plugin
        options: {
            reset: grunt.option('reset') || false,
            stoponerror: false,
            remotePath: '',
            doctype: 'HTML5',
            failHard: true,
            relaxerror: ["Bad value X-UA-Compatible for attribute http-equiv on element meta.","Element title must not be empty."]
        },
        files: {
            src: ['*.html']
        }
    },
    'sftp-deploy': {
      build: {
        auth: {
          host: 'alterego-russia.ru',
          port: 22,
          authKey: 'key1'
        },
        src: './',
        dest: './alteasy-html/',
        exclusions: ['./.ftppass', './.git', './.idea', './node_modules','./task.js','./wercker.yml', './.idea']
      }
    }
  });
  grunt.loadNpmTasks('grunt-w3c-html-validation');
  // grunt.loadNpmTasks('grunt-ftp-deploy');
  grunt.loadNpmTasks('grunt-sftp-deploy');
  grunt.registerTask('default', ['sftp-deploy']); //'validation',
};