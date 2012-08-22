#!/usr/bin/env ruby
# -*- ruby encoding: utf-8 -*-

require 'tinkerforge/ip_connection'

include Tinkerforge

HOST = 'localhost'
PORT = 4223

# Create IP connection to brickd
ipcon = IPConnection.new HOST, PORT

# Enumerate Bricks and Bricklets
ipcon.enumerate do |uid, name, stack_id, is_new|
  if is_new
    puts 'New device:'
  else
    puts 'Removed device:'
  end

  puts " Name:     #{name}"
  puts " UID:      #{uid}"
  puts " Stack ID: #{stack_id}"
  puts ''
end

puts 'Press key to exit'
$stdin.gets
ipcon.destroy
