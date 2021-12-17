---
title: "Belongie Lab - Team"
layout: gridlay
excerpt: "Belongie Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

## Faculty
{% assign number_printed = 0 %}
{% for member in site.data.faculty_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <br>email: <{{ member.email }}></i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Postdoc

<div class="row">

{% for member in site.data.postdoc_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <h5> <a href="{{ member.website }}">Personal website</a> </h5>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

## PhD Students

<div class="row">

{% for member in site.data.phd_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <h5> <a href="{{ member.website }}">Personal website</a> </h5>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

## Research Assistant

<div class="row">

{% for member in site.data.ra_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <h5> <a href="{{ member.website }}">Personal website</a> </h5>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

##  Alumni
<div class="row">

<div class="col-sm-6 clearfix">
<h4> <b>Cornell SE(3) PhD Alumni</b> </h4>
{% for member in site.data.se3_alumni %}
{{ member.name }}, {{ member.year }}. {{ member.next }} 
{% endfor %}
  <h4><b>Cornell BS/Masters Alumni & Visitors</b></h4>
  Pragya Verman<br>
  Philip Su<br>
  Andrew Mendez<br>
  Debarun Dhar<br>
  Tomáš Matera<br>
  Bicheng Gao<br>
  Xiaoyan Wu<br>
  Jiaqi Su<br>
  Sam Hoffman<br>
  Dilip Thiagarajan<br>
  Alvin Zhu<br>
  Isay Katsman<br>
  Xi Chen<br>
  Tharun Sankar<br>
  Jeremy Feinstein<br>
  Rohit Jain<br>
  Jonathan Huang<br>
  Arnaud Brejeon<br>
  Jan Jakeš<br>
  Daniel Glasner<br>
  Baoguang Shi<br>
  Chensu Xie<br>
  Yiwei Bai<br>
  Yurong Yu<br>
</div>

<div class="col-sm-6 clearfix">
<h4> <b>UCSD SO(3) PhD Alumni</b> </h4>
{% for member in site.data.so3_alumni %}
{{ member.name }}, {{ member.year }}. {{ member.next }} 
{% endfor %}
  <h4><b>UCSD BS/Masters Alumni & Visitors</b></h4>
  Grant Van Horn<br>
  Phuc X. Nguyen<br>
  Andrew Ziegler<br>
  Prasanna Krishnasamy<br>
  Nick True<br>
  Tess Winlock<br>
  Fred Birchmore<br>
  Nadav Ben-Haim<br>
  Tom Duerig<br>
  Louka Dlagnekov<br>
  Diem Vu<br>
  Stine Harder<br>
  Tomas Matera<br>
  Chong Cao<br>
  Antoni Chan<br>
  Kyong Mu Lee<br>
  Ana Cristina Murillo<br>
  Kris Kitani<br>
  Tsubasa Yoshida<br>
  Peter Faymonville<br>
  Masaaki Kokawa<br>
  Valentin Leonardi<br>
  Michele Merler<br>
  Jocelyn Cambria<br>
  Robin Hewitt<br>
  John Miller<br>
  Stephan Steinbach<br>
</div>

</div>

