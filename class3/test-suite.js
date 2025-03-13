const test = require('node:test');
const assert = require('assert/strict');

const Rational = require('./Rational'); // Assuming Rational.js is in the same directory

test('gcd(6,14)', function() {
    return assert.equal(Rational.gcd(6, 14), 2);
});

test('no args', function() {
    let f = new Rational();
    let s = f.toString();
    return assert.equal(s, '0');
});

test('3', function() {
    let f = new Rational(3);
    return assert.equal(f.toString(), '3');
});

test('3/7', function() {
    let f = new Rational(3, 7);
    return assert.equal(f.toString(), '3/7');
});

test('-3/7', function() {
    let f = new Rational(-3, 7);
    return assert.equal(f.toString(), '-3/7');
});

test('3/-7 => -3/7', function() {
    let f = new Rational(3, -7);
    return assert.equal(f.toString(), '-3/7');
});

test('6/-14 => -3/7', function() {
    let f = new Rational(6, -14);
    return assert.equal(f.toString(), '-3/7');
});

test('-3', function() {
    let f = new Rational(-3);
    return assert.equal(f.toString(), '-3');
});

test('3/7 + 1/8 => 31/56', function() {
    let f = new Rational(3, 7);
    let o = new Rational(1, 8);
    return assert.equal(f.add(o).toString(), '31/56');
});

test('3/7 - 1/8 => 17/56', function() {
    let f = new Rational(3, 7);
    let o = new Rational(1, 8);
    return assert.equal(f.sub(o).toString(), '17/56');
});

test('3/7 * 1/8 => 3/56', function() {
    let f = new Rational(3, 7);
    let o = new Rational(1, 8);
    return assert.equal(f.mul(o).toString(), '3/56');
});

test('3/7 / 1/8 => 24/7', function() {
    let f = new Rational(3, 7);
    let o = new Rational(1, 8);
    return assert.equal(f.div(o).toString(), '24/7');
});

test('3/4 > 2/3 -> 1', function() {
    let f = new Rational(3, 4);
    let o = new Rational(2, 3);
    return assert.equal(f.cmp(o), 1);
});

test('2/3 = 2/3 -> 0', function() {
    let f = new Rational(2, 3);
    let o = new Rational(2, 3);
    return assert.equal(f.cmp(o), 0);
});

test('2/3 < 3/4 -> -1', function() {
    let f = new Rational(2, 3);
    let o = new Rational(3, 4);
    return assert.equal(f.cmp(o), -1);
});

test('clone 3/7 with 6/7 / 2', function() {
    let f = new Rational(3, 7);
    let o = new Rational(6, 7);
    let p = new Rational(2);
    let q = o.div(p);
    return assert.equal(q.cmp(f), 0);
});

// Fixed the equality check for the Rational instance
test('2/3 is', function() {
    let f = new Rational(2, 3);
    let o = f;
    return assert.equal(f.equals(o), true);
});
