'use strict';

var gulp = require('gulp');
var connect = require('gulp-connect');
var webpack = require('gulp-webpack');
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');
var react = require('gulp-react');
var scsslint   = require('gulp-scss-lint');
var concat = require('gulp-concat')
var path = require('path');

// Initialize watch tasks
gulp.task('watch', ['run'], function() {
  gulp.watch(['./src/**/*.js'], ['concat']);
  gulp.watch(['./src/**/*.scss'], ['sass']);
});

// Build files for distribution
gulp.task('webpack', function() {
  return gulp.src('./src/js/app.js')
    .pipe(webpack({
      entry: {
        src: ['./src/js/app.js']
      },

      output: {
        path: path.resolve(__dirname, 'build'),
        filename: 'bundle.js'
      },

      resolve: {
        extensions: ['', '.js', '.jsx']
      }
      //
      //module: {
      //  loaders: [
      //    { test: /\.js$/, loader: 'jsx-loader!babel-loader' },
      //    { test: /\.css$/, loader: 'style-loader!css-loader' }
      //  ]
      //}
    }))
    .pipe(gulp.dest('dist/'))
    .pipe(connect.reload());
});


gulp.task('concat', function () {
  gulp.src('./src/js/*.js')
    .pipe(concat('app.js'))
    .pipe(gulp.dest('./dist/js'));
});


gulp.task('sass', function () {
  gulp.src('./src/sass/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./dist/css'));
});

// Run example server
gulp.task('run', ['build'], function(){
  connect.server({
    root: './dist',
    port: 8090,
    livereload: true
  });
});

gulp.task('react', function () {
  return gulp.src('./src/js/*.jsx')
    .pipe(react())
    .pipe(gulp.dest('dist'));
});

gulp.task('default', ['watch']);

gulp.task('build', ['webpack', 'sass', 'concat']);



