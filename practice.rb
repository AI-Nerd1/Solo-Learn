def demo(x)
    x+=4
    return x+2
    x+=1
  end
  puts demo(2)


  a = 2
loop do
  puts a
  a += 3
  break if a > 8
end


class A
    @num = 8
    def show
        puts @num
    end
end
class B < A
    def initialize
        @num = 2
    end
end
ob = B.new
ob.show


def x(y)
    res = 0
    (0..y).each {|z| res+=z}
    res
  end
  puts x(3)


a = 4
puts a**2

#square root
puts Math.sqrt(9)

#pi constant
puts Math::PI

#trigonometry (sin, cos, tan)
puts Math::cos(0)


#current time
t = Time.now
puts t.inspect

#year, month, day
puts t.year
puts t.month
puts t.day

#custom date
t = Time.new(1988, 6, 10)

#day of week: 0 is Sunday
puts t.wday

#day of year
puts t.yday

greet = Proc.new do |x|
    puts "Welcome #{x}"
  end

  greet = Proc.new do |x|
    puts "Welcome #{x}"
  end
  
  goodbye = Proc.new do |x|
    puts "Goodbye #{x}"
  end
  
  def say(arr, proc)
    arr.each { |x| proc.call x}
  end

  def calc(proc)
    start = Time.now
    proc.call
    dur = Time.now - start
  end

  def calc(proc)
    start = Time.now
    proc.call
    dur = Time.now - start
end

someProc = Proc.new do
    num = 0
    1000000.times do
      num = num + 1
    end
end

puts calc(someProc)

talk = ->() {puts "Hi" }
talk.call

a = lambda {|x| x*3}
puts a.call 6

Addr = Struct.new(:a, :b, :c)
a = Addr.new(3, 5, 2)
puts a.b

a=lambda{|x, y| x/y}
puts a.call 7, 2

file = File.new("test.txt", "w+")
file.close
file = File.new("test.txt", "w+")
file.puts("some text")
file.close

File.open("file.txt", "w+") {
  |file| file.puts("some text") 
}

f = File.new("test.txt", "w+")
f.puts("a line of text")
f.puts("another line of text")
f.close

puts File.read("test.txt")
File.open("test.txt") if File.file?("text.txt")


f = File.new("test.txt", "w+")
f.puts("some file content")

puts f.size

f.close

puts File.zero?("test.txt")


f = File.new("sample.txt", "w+")
f.write("start")
14.times do
  f.puts("hi")
end
f.write("end")
f.close