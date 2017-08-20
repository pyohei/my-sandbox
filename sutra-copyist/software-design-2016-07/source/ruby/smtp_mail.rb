#!/usr/local/bin/ruby

# -*- encoding: utf-8 -*-

require 'net/smtp'
require 'time'
require 'kconv'

# 設定
smtp_options = { 
  :host    => "mailserver.host",
  :port    => 587,
  :domain  => 'mailserver.host',
  :user    => 'username',
  :passwd  => 'P@ssword',
  :from    => "from-user@mailaddress.jp",
  :to      => "to-user@mailaddress.jp",
  :subject => "Mail Subject",
}

# 送信するメッセージ（本文は標準入力から受け取る）
send_message = <<EOM
From: #{smtp_options[:from]}
To: #{smtp_options[:to]}
Subject: #{smtp_options[:subject]}
Date: #{Time.now.rfc822}
MIME-Version: 1.0
Content-Type: text/plain; charset=ISO-2022-JP
Content-Transfer-Encoding: 7bit

#{$stdin.read}
EOM

Net::SMTP.start(smtp_options[:host], smtp_options[:port], smtp_options[:domain], smtp_options[:user], smtp_options[:pass]) do |smtp|
    smtp.send_mail send_message, smtp_options[:from], smtp_options[:to]
end
