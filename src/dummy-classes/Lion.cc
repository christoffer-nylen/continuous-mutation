#include "Lion.h"

Lion::Lion(int number_of_legs) :
  Feline(number_of_legs)
{}

bool Lion::isScaredOf(Feline feline) {
  (void)feline;
  return false;
}
