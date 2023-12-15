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
    const temp = this.width;
	this.width = this.height;
	this.height = temp;
    }

  double () {
	this.width *= 2;
	this.height *= 2;
  }
}

module.exports = Rectangle;
