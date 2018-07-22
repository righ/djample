const path = require('path');
const webpack = require('webpack');

module.exports = {
  context: __dirname,
  entry: path.resolve('./entry.js'),
  output: {
    path: path.resolve('./assets/'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
      },
      {
        test: /\.styl$/,
        use: ['stylus-loader'],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader?modules'],
      },
    ]
  },
  plugins: [
  ]
};
