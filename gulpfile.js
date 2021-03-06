var gulp = require('gulp'),
    rimraf = require('rimraf'),
    compass = require('gulp-compass'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    ignore = require('gulp-ignore'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    browserSync = require('browser-sync').create(),
    runSequence = require('run-sequence'),
    imagemin = require('gulp-imagemin')
    favicons = require('gulp-favicons'),
    gutil = require('gulp-util'),
    copy = require('gulp-copy'),
    plumber = require('gulp-plumber'),
    autoprefixer = require('gulp-autoprefixer'),
    browserify = require('gulp-browserify'),
    sourcemaps = require('gulp-sourcemaps');


// var srcFolder = 'app/themes/manifeste2017/static/src/',
//     destFolder = 'app/themes/manifeste2017/static/'

gulp.task('copy-assets-img', function() {
    gulp.src([srcFolder + 'assets/img/**/*'])
        .pipe(gulp.dest(destFolder + 'img'));
});

gulp.task('copy-vendors-js', function() {
    gulp.src([srcFolder + 'js/vendors/**/*'])
        .pipe(gulp.dest(destFolder + 'js'));
});

gulp.task("favicons", function () {
    return gulp.src(srcFolder + "assets/favicon/favicon.png")
        .pipe(favicons({
            background: "#ffffff",
            path: "/favicons/",
            replace: true,
            icons: {
                android: false,              // Create Android homescreen icon. `boolean`
                appleIcon: true,            // Create Apple touch icons. `boolean`
                appleStartup: false,         // Create Apple startup images. `boolean`
                coast: false,                // Create Opera Coast icon. `boolean`
                favicons: true,             // Create regular favicons. `boolean`
                firefox: false,              // Create Firefox OS icons. `boolean`
                opengraph: false,            // Create Facebook OpenGraph image. `boolean`
                twitter: false,              // Create Twitter Summary Card image. `boolean`
                windows: false,              // Create Windows 8 tile icons. `boolean`
                yandex: false                // Create Yandex browser icon. `boolean`
            }
        }))
        .on("error", gutil.log)
        .pipe(gulp.dest(destFolder + '/img/favicons/'));
});

gulp.task('main-js', function() {
    return gulp.src(srcFolder + 'js/index.js')
        .pipe(plumber({
            errorHandler: function (error) {
                console.log(error.message);
                this.emit('end');
            }})
        )
        .pipe(browserify({
		  insertGlobals : true,
		  debug : false
		}))
        .pipe(rename('index.min.js'))
        .pipe(sourcemaps.init())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'js'))
        .pipe(browserSync.stream());
});

gulp.task('main-css', function() {
    return gulp.src(srcFolder + 'sass/*.scss')
        .pipe(plumber({
            errorHandler: function (error) {
                this.emit('end');
            }})
        )
        .pipe(compass({
            css: './.tmp/main',
            sass: srcFolder + 'sass'
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.init())
        .pipe(autoprefixer())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'css'))
        .pipe(browserSync.stream());
});

gulp.task('starts-main-css', function() {
    return gulp.src(startsSrcFolder + 'sass/*.scss')
        .pipe(plumber({
            errorHandler: function (error) {
                this.emit('end');
            }})
        )
        .pipe(compass({
            css: './.tmp/starts-main',
            sass: startsSrcFolder + 'sass'
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.init())
        .pipe(autoprefixer())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(startsDestFolder + 'css'))
        .pipe(browserSync.stream());
});

gulp.task('vertigo-main-css', function() {
    return gulp.src(vertigoSrcFolder + 'sass/*.scss')
        .pipe(plumber({
            errorHandler: function (error) {
                this.emit('end');
            }})
        )
        .pipe(compass({
            css: './.tmp/vertigo-main',
            sass: vertigoSrcFolder + 'sass'
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.init())
        .pipe(autoprefixer())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(vertigoDestFolder + 'css'))
        .pipe(browserSync.stream());
});

gulp.task('cssmin', function() {
    return gulp.src(destFolder + 'css/**/*.css')
        .pipe(sourcemaps.init())
        .pipe(cssnano())
        .on("error", gutil.log)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'css/'))
        .pipe(browserSync.stream());
});

gulp.task('starts-cssmin', function() {
    return gulp.src(startsDestFolder + 'css/**/*.css')
        .pipe(sourcemaps.init())
        .pipe(cssnano())
        .on("error", gutil.log)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(startsDestFolder + 'css/'))
        .pipe(browserSync.stream());
});

gulp.task('vertigo-cssmin', function() {
    return gulp.src(vertigoDestFolder + 'css/**/*.css')
        .pipe(sourcemaps.init())
        .pipe(cssnano())
        .on("error", gutil.log)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(vertigoDestFolder + 'css/'))
        .pipe(browserSync.stream());
});

gulp.task('jsmin', function() {
    return gulp.src(destFolder + 'js/**/*.js')
        .pipe(sourcemaps.init())
        .pipe(uglify({'mangle': false}))
        .on("error", gutil.log)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'js/'))
        .pipe(browserSync.stream());
});

gulp.task('imagemin', function() {
	return gulp.src(destFolder + 'img/**/*')
		.pipe(imagemin({
			progressive: true,
            optimizationLevel: 3
		}))
        .on("error", gutil.log)
		.pipe(gulp.dest(destFolder + 'img'));
});

gulp.task('clean', function(cb) {
    rimraf('.tmp', cb);
});

gulp.task('serve', ['clean'], function () {

    browserSync.init({
        proxy: "http://localhost:9021/"
    });

    gulp.watch(srcFolder + 'assets/img/**/*', ['copy-assets-img']).on('change', browserSync.reload);
	gulp.watch(srcFolder + 'js/**/*.js', ['main-js']);
	gulp.watch(srcFolder + 'sass/**/*.scss', ['main-css']);
    gulp.watch(startsSrcFolder + 'sass/**/*.scss', ['starts-main-css']);
    gulp.watch(vertigoSrcFolder + 'sass/**/*.scss', ['vertigo-main-css']);

});

gulp.task('default', ['main-js', 'main-css', 'starts-main-css', 'vertigo-main-css', 'copy-assets-img', 'copy-vendors-js', 'serve']);
gulp.task('build', ['main-js', 'main-css', 'starts-main-css', 'vertigo-main-css', 'copy-assets-img', 'copy-vendors-js'], function() {
    runSequence(['cssmin', 'starts-cssmin', 'vertigo-cssmin', 'jsmin', 'imagemin', 'favicons', 'clean']);
});
