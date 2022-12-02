rm *.out
scancel `sq | grep _ | grep -v -e TIME | awk '{print $1}'`
rm ./see-segment/Image_data/Examples/*.txt
sbatch runExamples.sb
