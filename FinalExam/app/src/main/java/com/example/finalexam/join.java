package com.example.finalexam;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class join extends AppCompatActivity {

    EditText id, pw, nick, email;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_join);

        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();

        Button join = findViewById(R.id.joinBtn);
        id = findViewById(R.id.id);
        pw = findViewById(R.id.password);
        nick = findViewById(R.id.nickname);
        email = findViewById(R.id.email);

        join.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String idString = id.getText().toString().trim();
                String pwString = pw.getText().toString().trim();
                String nickString = nick.getText().toString().trim();
                String emailString = email.getText().toString().trim();

                Intent intent = new Intent(join.this, MainActivity.class);
                intent.putExtra("id", idString);
                intent.putExtra("pw", pwString);
                intent.putExtra("nickname", nickString);
                intent.putExtra("email", emailString);
                startActivity(intent);

            }
        });
    }
}