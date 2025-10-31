resource "aws_key_pair" "dove-key" {
  key_name   = "dove-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGVxZ7sKA1tgahNxuct4eo3S9DMY4c3Y6kRd03+4edrL LENOVO@DESKTOP-NCM15C8"
  # The public key above is for demonstration purposes only. In a real scenario, use your own public key.
  # To generate a new SSH key pair, you can use the ssh-keygen command and then cat the public key file to get the public key string.
}