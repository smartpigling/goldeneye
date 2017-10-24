/*
 * Main Javascript file for goldeneye.
 *
 * This file bundles all of your javascript together using webpack.
 */


// JavaScript modules
require('jquery');
require('font-awesome-webpack');
require('bootstrap');
require('fastclick/lib/fastclick');
require('jquery-sparkline/jquery.sparkline');
require('jvectormap/jquery-jvectormap');
require('jquery-slimscroll/jquery.slimscroll');
require('admin-lte/dist/js/adminlte');

// Your own code
require('./plugins.js');
require('./script.js');