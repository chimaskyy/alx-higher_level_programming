#!/usr/bin/node

// reverse a list

exports.esrever = function (list) {
  const lenList = list.length;
  const newList = [];
  for (let i = 0; i < lenList; i++) {
    newList[i] = list[lenList - i - 1];
  }
  return newList;
};
