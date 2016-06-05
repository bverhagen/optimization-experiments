Import('env')

import buildTools
import setupTools

benchmark_env = env.Clone()

setupTools.disableWarningAsError(benchmark_env)

# Download the library
benchmark_env.Command('benchmark/src/benchmark.cc', 'benchmark.commit', 'git submodule init 3rdparty/benchmark && git submodule update 3rdparty/benchmark')

# Build the library
cmake_options = [
    '-DBENCHMARK_ENABLE_TESTING=OFF',
    '-DBENCHMARK_ENABLE_LTO=OFF '
]

sources = [
    Glob('benchmark/src/*.cc'),
    Glob('benchmark/src/*.h')
]

lib = buildTools.buildCmake(    benchmark_env, 'libbenchmark.a', 
                                sources, 
                                '3rdparty/benchmark',
                                benchmark_env['THIRD_PARTY_DIR'] + '/benchmark', 
                                cmake_options,
                                'src/libbenchmark.a'
                        )
                            
installed_lib = benchmark_env.Install("{libs_dir}".format(libs_dir=env['THIRD_PARTY_LIBS_DIR']), lib)
benchmark_env.Alias('benchmark', installed_lib)
