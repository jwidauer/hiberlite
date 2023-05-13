cmake_minimum_required(VERSION 3.6)

project(hiberlite)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 11)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-terminate")

set(TARGET_NAME hiberlite)

set(SOURCES_SQLITE sqlite-amalgamation/sqlite3.c sqlite-amalgamation/sqlite3.h)

set(SOURCES
    src/BeanLoader.cpp
    src/BeanUpdater.cpp
    src/ChildKiller.cpp
    src/CppModel.cpp
    src/Database.cpp
    src/ModelExtractor.cpp
    src/Registry.cpp
    src/shared_res.cpp
    src/SQLiteStmt.cpp
    src/Visitor.cpp
    include/hiberlite/BeanLoader.h
    include/hiberlite/BeanLoader_impl.hpp
    include/hiberlite/BeanUpdater.h
    include/hiberlite/BeanUpdater_impl.hpp
    include/hiberlite/ChildKiller.h
    include/hiberlite/ChildKiller_impl.hpp
    include/hiberlite/CppModel.h
    include/hiberlite/Database.h
    include/hiberlite/Database_tmpl_impl.hpp
    include/hiberlite/ModelExtractor.h
    include/hiberlite/ModelExtractor_impl.hpp
    include/hiberlite/Registry.h
    include/hiberlite/Registry_impl.hpp
    include/hiberlite/SQLiteStmt.h
    include/hiberlite/UpdateVisitor_tmpl.hpp
    include/hiberlite/Visitor.h
    include/hiberlite/Visitor_tmpl_impl.hpp
    include/hiberlite/bean_ptr.h
    include/hiberlite/bean_ptr_impl.hpp
    include/hiberlite/common.h
    include/hiberlite/db_error.h
    include/hiberlite/hiberdefs.h
    include/hiberlite/hiberlite.h
    include/hiberlite/nvp.h
    include/hiberlite/shared_res.h
    include/hiberlite/some_types.h
)

add_library(${TARGET_NAME} ${SOURCES} ${SOURCES_SQLITE})

target_include_directories(${TARGET_NAME} PUBLIC include sqlite-amalgamation)

target_link_libraries(${TARGET_NAME} pthread dl)

add_executable(sample apps/sample/sample.cpp)

target_link_libraries(sample ${TARGET_NAME})

add_executable(tests test/tests.cpp)

target_link_libraries(tests ${TARGET_NAME})
