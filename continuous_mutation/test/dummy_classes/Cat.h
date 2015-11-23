#ifndef CAT_H
#define CAT_H

class Cat;

#include "Feline.h"

class Cat : public Feline {
public:
  Cat(int number_of_legs);
  ~Cat() = default;

  virtual bool isScaredOf(Cat cat);
  virtual bool isScaredOf(Feline feline);
};

#endif /* CAT_H */
