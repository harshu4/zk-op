import subprocess
import os

def run_command(command, description):
    print(f"Running: {description}")
    print(f"Command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Output:\n{result.stdout}")
    if result.stderr:
        print(f"Error:\n{result.stderr}")
    print("-" * 40)

def main():
    # Change to the first layer directory and run the first 3 layers
    os.chdir('output/circuit_first.circom')
    
    run_command("cd output/circuit_first.circom", "Changing directory to 'first_threelayers'")
    run_command("python .\\circuit.py .\\circuit.json .\\input.json -o .\\output", "Running first 3 layers")
    run_command("python ..\\tau\\merger.py", "Merging input and output to generate proof")
    run_command("snarkjs wtns calculate circuit_js/circuit.wasm final.json witness.wtns", "Calculating witness")
    run_command("snarkjs groth16 prove circuit_0001.zkey witness.wtns proof.json public.json", "Proving the input and output for first 3 layers")
    run_command("snarkjs groth16 verify verification_key.json public.json proof.json", "Running the verify command for first 3 layers")

    # Change to the last layer directory and run the last 3 layers
    os.chdir('../circuit_last.circom')

    run_command("cd ../circuit_last.circom", "Changing directory to 'last_threelayers'")
    run_command("python .\\circuit.py .\\circuit.json .\\input.json -o .\\output", "Running last 3 layers")
    run_command("python ..\\tau\\merger.py", "Merging input and output to generate proof for last 3 layers")
    run_command("snarkjs wtns calculate circuit_js/circuit.wasm final.json witness.wtns", "Calculating witness for last 3 layers")
    run_command("snarkjs groth16 prove circuit_0001.zkey witness.wtns proof.json public.json", "Proving the input and output for last 3 layers")
    run_command("snarkjs groth16 verify verification_key.json public.json proof.json", "Running the verify command for last 3 layers")

if __name__ == "__main__":
    main()
