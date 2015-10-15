#ifndef LION_H
#define LION_H

class Lion;

#include "Feline.h"

class Lion : public Feline {
public:
  Lion(int number_of_legs);
  ~Lion() = default;

  virtual bool isScaredOf(Feline feline);
};

#endif /* LION_H */
