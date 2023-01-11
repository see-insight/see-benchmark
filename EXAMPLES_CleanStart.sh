rm ./Benchmark_Examples/*.out
scancel `sq | grep _ | grep -v -e TIME | awk '{print $1}'`
rm ./see-segment/Image_data/Examples/*.txt
sbatch EXAMPLES_batch.sh 

