require 'spec_helper'

describe 'webservice', :type => 'class' do
  context 'install python-pip' do
    it { should contain_package('python') }
  end
  context 'install python' do
    it { should contain_package('python-pip') }
  end
  context 'install python-setuptools' do
    it { should contain_package('python-setuptools') }
  end
end

