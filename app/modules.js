var sqlite3 =require('sqlite3').verbose();
var db = new sqlite3.Database(data_teams.db);

//Functions to get player info by team name

exports.getPlayerNames = function (var teamName) {
	var names = [];
	db.serialize(function () {
		db.each("SELECT name FROM players WHERE team="+teamName, function(err, row) {
			names.push(row.name);
		});
	});
	return names;
};

exports.getPlayerNumber = function(var playerName) {
	var num;
	db.serialize(function () {
		db.each("SELECT num FROM playeres WHERE name="+playerName), function(err, row) {
			num = row.num;
		});
	});
	return num;
};

exports.getPlayerPosition = function(var playerName) {
	var pos;
	db.serialize(function () {
		db.each("SELECT pos FROM players WHERE name="+playerName), function(err, row) {
			pos = row.pos;
		});
	});
	return pos;
};	

exports.getPlayerHeight = function(var playerName) {
	var height;
	db.serialize(function () {
		db.each("SELECT height FROM players WHERE name="+playerName), function(err, row) {
			height = row.height;
		});
	});
	return height;
};

exports.getPlayerWeight = function(var playerName) {
	var weight;
	db.serialize(function () {
		db.each("SELECT weight FROM players WHERE name="+playerName), function(err, row) {
			weight = row.weight;
		});
	});
	return weight;
};
		



























	
