#!/usr/bin/node

// reverse a list

exports.esrever = function (list) {
	let lenList = list.length;
	let new_list = []
	for (let i = 0; i < lenList; i++) {
		new_list[i] = list[lenList - i -1];
	}
	return new_list;
};