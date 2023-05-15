#ifndef COMMON_H_
#define COMMON_H_

#include <sqlite3.h>

#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

namespace hiberlite {

class noncopyable {
 protected:
  noncopyable() {}
  ~noncopyable() {}

 private:
  noncopyable(const noncopyable&);
  const noncopyable operator=(const noncopyable&);
};

typedef sqlite_int64 sqlid_t;

}  // namespace hiberlite

#define HIBERLITE_HL_DBG_DO(x) ;

#endif
