<?php

$lines = file_get_contents('php://stdin');
foreach (explode("\n", $lines) as $line) {
  $regex = '/^(\S+) (\S+) (\S+) \[([^:]+):(\d+:\d+:\d+) ([^\]]+)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) "([^"]*)" "([^"]*)"/';
  preg_match($regex ,$line, $matches);

  echo implode(",", $matches) . PHP_EOL;
}