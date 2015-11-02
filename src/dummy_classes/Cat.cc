#include "Cat.h"


Cat::Cat(int number_of_legs) :
  Feline(number_of_legs)
{}

bool Cat::isScaredOf(Cat cat) {
  (void)cat;
  return false;
}

bool Cat::isScaredOf(Feline feline) {
  (void)feline;
  return true;
}
