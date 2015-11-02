#ifndef CANINE_H
#define CANINE_H

class Canine;

#include "Feline.h"

#include "Animal.h"

class Canine : public Animal {
public:
  Canine(int number_of_legs);
  ~Canine() = default;

  virtual void cry();
  virtual int getNumberOfLegs();

  virtual bool isScaredOf(Feline feline);
  virtual bool isScaredOf(Canine canine);

protected:
  int number_of_legs;
};

#endif /* CANINE_H */
