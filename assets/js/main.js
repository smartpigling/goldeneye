/*
 * Main Javascript file for goldeneye.
 *
 * This file bundles all of your javascript together using webpack.
 */


// JavaScript modules
require('jquery');
require('font-awesome-webpack');
require('bootstrap');
require('admin-lte/dist/js/adminlte');
// require('fastclick/lib/fastclick');
// require('jquery-sparkline/jquery.sparkline');
// require('jvectormap/jquery-jvectormap');
// require('jquery-slimscroll/jquery.slimscroll');
// require('datatables.net/js/jquery.dataTables');
// require('datatables.net-bs/js/dataTables.bootstrap');
// require('icheck/icheck');

// Your own code
require('./plugins.js');
require('./script.js');