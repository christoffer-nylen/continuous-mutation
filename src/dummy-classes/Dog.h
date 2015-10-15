#ifndef DOG_H
#define DOG_H

#include "Canine.h"

class Dog : public Canine {
public:
  Dog(int number_of_legs);
  ~Dog() = default;

  virtual void cry();
};

#endif /* DOG_H */
