Import('env')

import my_utils

#lib = env.Command('libbenchmark.a', 'benchmark/src/benchmark.cc', 
#[
#    'echo "Building lib benchmark..."',
#    'mkdir -p ' + env['THIRD_PARTY_DIR'] + '/benchmark',
#    'cmake -B' + env['THIRD_PARTY_DIR'] + '/benchmark ' +
#        '-H3rdparty/benchmark -DCMAKE_BUILD_TYPE=release ' + 
#        '-DBENCHMARK_ENABLE_TESTING=OFF -DBENCHMARK_ENABLE_LTO=OFF ' +
#        '-DCMAKE_C_COMPILER=' + env['CC'] + ' ' +
#        '-DCMAKE_CXX_COMPILER=' + env['CXX'],
#    'make -C' + env['THIRD_PARTY_DIR'] + '/benchmark -j',
#    'cp ' + env['THIRD_PARTY_DIR'] + '/benchmark/src/libbenchmark.a $TARGET'
#])

cmake_options = [
    '-DBENCHMARK_ENABLE_TESTING=OFF',
    '-DBENCHMARK_ENABLE_LTO=OFF '
]

lib = my_utils.buildCmake(  env, 'libbenchmark.a', 
                            Glob('benchmark/src/*.cc'), 
                            '3rdparty/benchmark',
                            env['THIRD_PARTY_DIR'] + '/benchmark', 
                            cmake_options,
                            'src/libbenchmark.a'
                        )
                            
installed_lib = env.Install("{libs_dir}".format(libs_dir=env['THIRD_PARTY_LIBS_DIR']), lib)
env.Alias('benchmark', installed_lib)
