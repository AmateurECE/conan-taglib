///////////////////////////////////////////////////////////////////////////////
// NAME:            TagLibTest.cpp
//
// AUTHOR:          Ethan D. Twardy <edtwardy@mtu.edu>
//
// DESCRIPTION:     Package test for the TagLib Conan package.
//
// CREATED:         11/24/2020
//
// LAST EDITED:     11/24/2020
////

#include <cstring>
#include <taglib/tstring.h>

int main()
{
  TagLib::String message("Welcome to TagLib!\n");
  std::cout << message;
}

///////////////////////////////////////////////////////////////////////////////
