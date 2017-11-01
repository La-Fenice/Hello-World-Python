var mastercardfacts = []
mastercardfacts[0] = "Mastercards network maintains a processing performance of 130 milliseconds per transaction.";
mastercardfacts[1] = "Ajaypal Singh Banga is the current CEO.";
mastercardfacts[2] = "The Global Operations Headquarters is located in O'Fallon, Missouri.";
mastercardfacts[3] = "Mastercard has 11,900 employees!";
mastercardfacts[4] = "Mastercard Dublin currently employs 200 people!";
mastercardfacts[5] = "Mastercard's vision is based off the goal of making people's lives easier by applying the latest technologies to advanced payment systems and solutions.";
mastercardfacts[6] = "Mastercard connects 2 billion card holders to over 40 million merchants.";
mastercardfacts[7] = "Mastercard operates in over 200 countries!";
mastercardfacts[8] = "Mastercard have committed to getting 500 million people financially included by 2020.";


function getFact() {
  var randomNum = Math.floor(Math.random()*(mastercardfacts.length));
  document.getElementById('mfact').innerHTML = mastercardfacts[randomNum];
}
