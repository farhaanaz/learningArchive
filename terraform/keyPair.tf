resource "aws_key_pair" "dove-key" {
  key_name   = "its a secret LOL"
  public_key = "its a secret LOL"
  # The public key above is for demonstration purposes only. In a real scenario, use your own public key.
  # To generate a new SSH key pair, you can use the ssh-keygen command and then cat the public key file to get the public key string.
}
