#ifndef FELINE_H
#define FELINE_H

class Feline;

#include "Canine.h"

#include "Animal.h"

class Feline : public Animal {
public:
  Feline(int number_of_legs);
  ~Feline() = default;

  virtual void cry();
  virtual int getNumberOfLegs();

  virtual bool isScaredOf(Canine canine);
  virtual bool isScaredOf(Feline feline);

protected:
  int number_of_legs;
};

#endif /* FELINE_H */
