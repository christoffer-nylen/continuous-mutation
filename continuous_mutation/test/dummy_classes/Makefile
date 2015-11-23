CXXFLAGS = -Wall -Wextra -pedantic -Werror -std=c++11
SRCFILES = $(wildcard ./*.cc)
HEADERFILES = $(wildcard ./*.h)
OBJFILES = $(addsuffix .o, $(basename $(SRCFILES)))

all: $(OBJFILES)

clean:
	$(RM) $(OBJFILES)
