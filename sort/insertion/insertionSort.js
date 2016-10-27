Array.prototype.swap = function(a,b){
  console.log("swap a: ", this[a], ' swap b: ', this[b]);

  var tmp = this[a];
  this[a] = this[b];
  this[b] = tmp;
}

Array.prototype.generate_numbers = function(amount){
  for (var i = 0; i < amount; i++ ){
    this[i] = Math.floor(Math.random() * amount + 1);
  }
}

Array.prototype.knuth_shuffle = function() {
  var random = 0;
  for (var i = 1; i < this.length; i++){
    var random = Math.floor(Math.random() * i);
    this.swap(i, random);
  }
};

var insertion_sort = function(array){
  console.log('orriginal array: %o', array);
  var length = array.length;
  for (var i = 0; i < length; i++){
    console.log('iteration: i: %o', i);
    for ( var j = i; j > 0; j-- ){
      console.log('j: %o', j);
      if (array[j] < array[j-1] ){
        array.swap(j, j-1);
      } else {
        break;
      }
    }
  }
  return array;
}

console.log(insertion_sort([1, 90, 5, 77]));
