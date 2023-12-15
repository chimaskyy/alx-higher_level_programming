#!/usr/bin/node

/* Print rectangle
 * exchange the width and the height
 * multiply width and height by 2
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j, row;
    for (i = 0; i < this.height; i++) {
      row = '';
      for (j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    let i, j, row;
    for (i = 0; i < this.width * 2; i++) {
      row = '';
      for (j = 0; j < this.height * 2; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  double () {
    let i, j, row;
    for (i = 0; i < this.height * 2; i++) {
      row = '';
      for (j = 0; j < this.width * 2; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
