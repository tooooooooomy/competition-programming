class Yatzy
  def self.chance(*args)
    args.sum
  end

  def self.yatzy(dice)
    counts = [0]*(dice.length+1)
    for die in dice do
      counts[die-1] += 1
    end

    counts.any? { |c| c == 5 } ? 50 : 0
  end

  def self.ones(*args)
    self.counts(args, 1)
  end

  def self.counts(args, n)
    args.select {|die| die == n }.sum
  end

  def self.twos(*args)
    self.counts(args, 2)
  end

  def self.threes(*args)
    self.counts(args, 3)
  end

  def initialize(d1, d2, d3, d4, _5)
    @dice = [0]*5
    @dice[0] = d1
    @dice[1] = d2
    @dice[2] = d3
    @dice[3] = d4
    @dice[4] = _5
  end

  def counts(n)
    @dice.select {|die| die == n }.length * n
  end

  def fours
    counts(4)
  end

  def fives()
    counts(5)
  end

  def sixes
    counts(6)
  end

  def self.score_pair(*dice)
    counts = {}
    dice.each do |die|
      if counts.key?(die)
        counts[die] += 1
      else
        counts[die] = 1
      end
    end

    if counts.any? { |die, c| c >= 2 }
      counts.select { |die, c| c >= 2 }.keys.max * 2
    else
      0
    end
  end

  def self.two_pair(*dice)
    counts = {}
    dice.each do |die|
      if counts.key?(die)
        counts[die] += 1
      else
        counts[die] = 1
      end
    end

    pairs = counts.select { |die, c| c >= 2 }.keys
    return 0 if pairs.size != 2

    pairs.sum * 2
  end

  def self.four_of_a_kind(*dice)
    self.n_of_a_kind(dice, 4)
  end

  def self.three_of_a_kind(*dice)
    self.n_of_a_kind(dice, 3)
  end

  def self.n_of_a_kind(dice, n)
    counts = {}
    dice.each do |die|
      if counts.key?(die)
        counts[die] += 1
      else
        counts[die] = 1
      end
    end

    counts.find { |die, c| c >= n }[0] * n || 0
  end


  def self.smallStraight(*dice)
    dice.uniq.length == 5 ? 15 : 0
  end

  def self.largeStraight(*dice)
    dice = dice.uniq.sort
    return 0 if dice.length != 5

    (dice.first == 2 and dice.last == 6) ? 20 : 0
  end

  def self.fullHouse(*dice)
    count = {}
    for die in dice
      if count[die]
        count[die] += 1
      else
        count[die] = 1
      end
    end

    return 0 if count.length != 2

    count.sum {|die, c| die * c }
  end
end
