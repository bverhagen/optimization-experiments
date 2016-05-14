Import('env')

import buildTools

cmake_options = [
    '-DBENCHMARK_ENABLE_TESTING=OFF',
    '-DBENCHMARK_ENABLE_LTO=OFF '
]

lib = buildTools.buildCmake(    env, 'libbenchmark.a', 
                                Glob('benchmark/src/*.cc'), 
                                '3rdparty/benchmark',
                                env['THIRD_PARTY_DIR'] + '/benchmark', 
                                cmake_options,
                                'src/libbenchmark.a'
                        )
                            
installed_lib = env.Install("{libs_dir}".format(libs_dir=env['THIRD_PARTY_LIBS_DIR']), lib)
env.Alias('benchmark', installed_lib)
